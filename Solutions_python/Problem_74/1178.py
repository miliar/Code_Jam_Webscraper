import sys

class Robot(object):
	ORANGE = 'O'
	BLUE   = 'B'

	@classmethod
	def opposite_colour(clazz, colour_):
		if colour_ == clazz.ORANGE:
			return clazz.BLUE
		if colour_ == clazz.BLUE:
			return clazz.ORANGE

		return None

	def __init__(self):
		self._current_button = 1
		self._next_buttons = []

	def add_next_button(self, button_):
		self._next_buttons.append(button_)

	def has_next_button(self):
		return len(self._next_buttons) != 0

	def press_next_button(self):
		assert(len(self._next_buttons) != 0)

		if self._current_button != self._next_buttons[0]:
			raise Exception('Cannot press button if not next to it')

		self._next_buttons.pop(0)

	def at_next_button(self):
		assert(len(self._next_buttons) != 0)

		return self._current_button == self._next_buttons[0]

	def advance_to_next_button(self):
		assert(len(self._next_buttons) != 0)

		next_button = self._next_buttons[0]
		if next_button > self._current_button:
			self._current_button += 1
		elif next_button < self._current_button:
			self._current_button -= 1 

class Runner(object):
	def __init__(self, file_):
		self._test_cases = None # list<list<tuple<int, colour>>>

		with open(file_) as f:
			for line in f:
				if self._test_cases == None:
					self._test_cases = []
				else:
					raw = line.split(' ')[1:]
					test_case = []
					for i in range(0, len(raw)/2):
						index = i * 2
						test_case.append(tuple([raw[index], int(raw[index+1])]))
					self._test_cases.append(test_case)

#		print self._test_cases

	def run(self):
		for i, t in enumerate(self._test_cases):
			robots = {Robot.BLUE: Robot(), Robot.ORANGE: Robot()}
			for colour, button in t:
				robots[colour].add_next_button(button)

			time = 0
			for colour, button in t:
				button_pressed = False
				while not button_pressed:
					this_robot = robots[colour]
					if this_robot.at_next_button():
						this_robot.press_next_button()
						button_pressed = True
					else:
						this_robot.advance_to_next_button()

					other_robot = robots[Robot.opposite_colour(colour)]
					if other_robot.has_next_button() and not other_robot.at_next_button():
						other_robot.advance_to_next_button()

					time += 1

			print 'Case #%d: %d' % (i+1, time)

if __name__ == '__main__':
	Runner(sys.argv[1]).run()

#/usr/bin/python
import sys

class Robot(object):
    
    def __init__(self):
        self.current_position = 1
        self.current_button = 0
        self.buttons_to_press = []

    def move(self):
        if len(self.buttons_to_press) > self.current_button:
            if self.buttons_to_press[self.current_button] == self.current_position:
                return False
            elif self.buttons_to_press[self.current_button] > self.current_position:
                self.current_position += 1
                return True
            else:
                self.current_position -= 1
                return True
        else:
            return None

    def press_button(self):
        if len(self.buttons_to_press) > self.current_button:
            if self.buttons_to_press[self.current_button] == self.current_position:
                self.current_button += 1
                return True
            else:
                self.move()
        else:
            return None

    def add_button(self, button):
        self.buttons_to_press.append(button)
        
                
            

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    infile = sys.argv[1]
    print infile
    with open(infile) as f:
        num_tests = int(f.readline())
        print "number of tests: {0}".format(num_tests)
        case_number = 1
        solutions = {}
        for line in f:
            print "Solving case #{0}".format(case_number)
            splitline = line.split()
            num_buttons = int(splitline[0])
            splitline = splitline[1:]
            buttons_to_press = []
            blue = Robot()
            orange = Robot()
            for i in range(0,2*num_buttons,2):           
                r_name = splitline[i]
                b_num = int(splitline[i+1])
                buttons_to_press.append((r_name, b_num))
                if r_name == 'B':
                    blue.add_button(b_num)
                else:
                    orange.add_button(b_num)
            
            time = 0     
            for button in buttons_to_press:
                if button[0] == 'B':
                    while not blue.press_button():
                        orange.move()
                        time += 1
                    orange.move()
                    time += 1
                else:
                    while not orange.press_button():
                        blue.move()
                        time += 1
                    blue.move()
                    time += 1

            solutions[case_number] = time


            case_number += 1
    outfile = sys.argv[2]
    with open(outfile, 'w') as of:
        for solution in solutions:
            of.write('Case #{0}: {1}\n'.format(solution, solutions[solution]))

from __future__ import division

def get_test_cases():
	t = int(raw_input())
	for test_case in range(t):
		d, n = map(int, raw_input().split())
		horses = [[None, None] for i in range(n)]
		for i in range(n):
			horses[i] = map(int, raw_input().split())
		yield horses, d


def write_output(i, output):
	print "Case #{index}: {result:.6f}".format(index=i, result=output)


def change_to_opposite(pancake):
	return PANCAKE_POSITIONS[pancake]


def solve(horses, dest):
	max_time = 0
	for horse in horses:
		cur_time = (dest - horse[0]) / horse[1]
		max_time = max(max_time, cur_time)
	return dest / max_time


def main():
	for i, input_data in enumerate(get_test_cases(), start=1):
		write_output(i, solve(*input_data))


if __name__ == '__main__':
	main()
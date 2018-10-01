#!/usr/bin/python
import sys

def get_seconds_to_x(data):
	c = float(data[0])
	f = float(data[1])
	x = float(data[2])

	seconds = 0
	cookies_per_seconds = 2

	while True:
		if (x / cookies_per_seconds) <= ((c / cookies_per_seconds) + (x / (cookies_per_seconds + f))):
			seconds = seconds + (x / cookies_per_seconds)
			break

		seconds = seconds + c / cookies_per_seconds
		cookies_per_seconds = cookies_per_seconds + f

	return seconds

def main():
	filename = sys.argv[1:]
	f = open(filename[0])

	testcase = int(f.readline())

	for case in range(testcase):
		data = f.readline()
		datas = data.split()

		seconds_to_x = get_seconds_to_x(datas)

		print 'Case #{0}: {1}'.format(case + 1, seconds_to_x)


if __name__ == '__main__':
	main()
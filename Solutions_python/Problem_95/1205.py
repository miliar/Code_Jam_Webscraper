import fileinput
import sys

keycode = [
					('a','y'),
					('b','h'),
					('c','e'),
					('d','s'),
					('e','o'),
					('f','c'),
					('g','v'),
					('h','x'),
					('i','d'),
					('j','u'),
					('k','i'),
					('l','g'),
					('m','l'),
					('n','b'),
					('o','k'),
					('p','r'),
					('q','z'),
					('r','t'),
					('s','n'),
					('t','w'),
					('u','j'),
					('v','p'),
					('w','f'),
					('x','m'),
					('y','a'),
					('z','q'),
					(' ',' ')]

#for tup in keycode:
#	if tup[1] == 'temp':
#		print(tup[0])

i = 1
firstone = True
for line in fileinput.input():
	if firstone:
		firstone = False
		continue
	sys.stdout.write("Case #" + str(i) + ": ")
	for letter in line:
		for tup in keycode:
			if tup[0] == letter:
				sys.stdout.write(tup[1])
				break
	sys.stdout.write('\n')
	i+=1

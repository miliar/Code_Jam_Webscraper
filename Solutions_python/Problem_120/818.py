of = open('A-small-attempt0.txt', 'w')

f = open('A-small-attempt0.in', 'r')

counter = 0

number_of_test_cases = 0
row = 0

test_cases = []
bullseye = []

count_n = 0
r, t = 0, 0


for line in f:
    if counter==0:
        number_of_test_cases = int(line)
    else:
        r, t = map(int,line.rstrip('\n').split())
        bullseye.append(tuple([r, t]))
    counter += 1

if len(bullseye)<number_of_test_cases:
    bullseye.append(tuple([r, t]))

print len(bullseye)

if(len(bullseye)!=number_of_test_cases):
    raise ValueError('number of test cases read from file does not match the indicated number of test cases that should be there')

f.close()

pain_needed = 0
odd_counter = 1
counter = 0

for case_num in range(len(bullseye)):
    r, t = bullseye[case_num]

    pain_needed = 0
    odd_counter = 1
    counter = 0
    prev_Area = r*r

    while pain_needed < t:
        Area = r*(r + 2*odd_counter) + odd_counter*odd_counter
        pain_needed += Area - prev_Area

        even_counter = odd_counter+1
        prev_Area = Area + 2*(r+odd_counter) + 1

        counter += 1
        odd_counter += 2

    if pain_needed>t:
        counter -= 1

    print 'Case #%d: %d'%(case_num+1, counter)
    of.write('Case #%d: %d'%(case_num+1, counter))

    of.write('\n')
of.close()

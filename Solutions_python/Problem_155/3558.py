import sys

if __name__ == '__main__':
    filename = sys.argv[1]
    test_cases = open(filename)
    answer = open(filename + '_solution', 'w')
    count = test_cases.readline()
    for i in range(0, int(count)):
        aud_count, shyness = test_cases.readline().split(' ')
        shyness_arr = map(int, list(shyness.strip()))
        people_clapping = 0
        people_needed = 0
        for (shyness, shy_card) in enumerate(shyness_arr):
            if( shyness > people_clapping):
                add_people = shyness - people_clapping
                people_needed+=add_people
                people_clapping+=add_people
            people_clapping+=shy_card
        answer.write("Case #{0}: {1}\n".format(i+1, people_needed))

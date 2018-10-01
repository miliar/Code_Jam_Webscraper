__author__ = 'Orin'

def main():
    folder = 'C:\\Users\\New Editor\\Documents\\orin\\GoogleCodeJam\\2015\\QualificationRound\\'
    input_path = 'A-large.in'
    out_path = 'A-large-out.txt'
    with open(folder + input_path, 'r') as input_file:
        inp = input_file.read()

    #splits into the string into cases and removes the case numbers from the list
    inp = inp.split('\n')
    cases = int(inp[0])
    inp.remove(inp[0])

    #splits the each case into the max shyness and the people array
    for i in range(cases):
        inp[i] = inp[i].split(' ')

    with open(folder + out_path, 'w') as out_file:
        for c in range(cases):
            case = inp[c]
            maxShy = int(case[0])
            peopleList = case[1]
            clapping = 0
            needed = 0


            for shyNum in range(maxShy+1):

                #check if there are people in this shyness level
                if int(peopleList[shyNum]) != 0:

                    #checking if there are not enough so they would clap
                    if clapping < shyNum:
                        needed += shyNum - clapping
                        clapping += shyNum - clapping
                #adds the number of people clapping now
                clapping += int(peopleList[shyNum])
            out_file.write('Case #{0}: {1}\n'.format(c+1, needed))


if __name__ == '__main__':
    main()

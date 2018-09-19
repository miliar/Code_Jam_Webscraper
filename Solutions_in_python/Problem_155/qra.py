__author__ = 'jslivane'

import sys


def run():

    # filename = "testdata1.txt"
    filename = "A-small-attempt2.in"
    out_filename = filename.replace(".in", ".out")

    if len(sys.argv) >= 2:
        readfile(sys.argv[1])

    try:
        with open(filename) as inputdata:

            # print(inputdata.read())

            with open(out_filename, "w") as outputdata:

                noOfTestCases = int(inputdata.readline())
                #print("noOfTestCases = %d" % noOfTestCases)

                for i in range(0, noOfTestCases):
                    noOfFriednsToInvite = 0
                    accNoOfPeoples = 0

                    linedata = inputdata.readline()
                    splitLinedata = linedata.split(" ")
                    maxShynessLevel = int(splitLinedata[0])
                    peoples = splitLinedata[1]

                    # print("Case #%d: %d, %s" % (i + 1, maxShynessLevel, peoples))

                    for j in range(0, maxShynessLevel + 1):
                        noOfPeople = int(peoples[j])
                        # print("%d, %d" % (j, noOfPeople))

                        if noOfPeople > 0 and accNoOfPeoples < j:
                            noOfFriednsToInvite += j - accNoOfPeoples
                            accNoOfPeoples += noOfFriednsToInvite

                        accNoOfPeoples += noOfPeople

                        # print("accNoOfPeoples=%d" % accNoOfPeoples)

                    # print("noOfFriednsToInvite=%d" % noOfFriednsToInvite)
                    # print("Case #%d: %d" % (i + 1, noOfFriednsToInvite))
                    outputdata.write("Case #%d: %d\n" % (i + 1, noOfFriednsToInvite))


                # for line in inputdata:
                #     print(line)

    except IOError as e:
        print('Unable to read file (%s)' % e.strerror)


if __name__ == '__main__':
    run()
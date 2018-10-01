"""
Jonathan Simowitz

Google Code Jam 2011
B. Magicka
"""

import os

"""
Funciton responsible for applying the algorithm
on the test data and returning the output
"""
def process(data):
    data = data.split(" ")
    num_combining = int(data.pop(0))
    #setup the combining dictionary
    combining_data = {}
    for i in range(num_combining):
        item = data.pop(0)
        combining_data[item[0:2]] = item[2]
        combining_data[item[1]+item[0]] = item[2]

    num_opposing = int(data.pop(0))
    #setup the opposition set
    opposing_data = {}
    for i in range(num_opposing):
        item = data.pop(0)
        opposing_data[item[0:2]] = True
        opposing_data[item[1]+item[0]] = True

    num_invoke = int(data.pop(0))
    current = 0
    data = data[0]
    spell_cast = []
    while current < num_invoke:
        spell_cast.append(data[current])
        current += 1
        spell_len = len(spell_cast)

        if (spell_len > 1):
            #apply combining
            try:
                spell_string = spell_cast[spell_len-2] + spell_cast[spell_len-1]
                #this throws exception if the two can't combine
                new_spell = combining_data[spell_string]
                
                spell_cast.pop(spell_len-1)
                spell_cast.pop(spell_len-2)
                spell_cast.append(new_spell)
            except:
                #spells can't combine, check if they oppose
                for i in range(spell_len-1):
                    if (opposing_data.has_key(spell_cast[i]+spell_cast[spell_len-1])):
                        spell_cast = []
                        break

    return str(spell_cast).replace("'","")

"""
Main function initializes files, iterates through
data, writes output, and closes the files.
"""
def main():
    #Open the input file
    rf = open(os.path.join(os.getcwd(), "B-large.in"), "r")
    #Open the output file
    wf = open(os.path.join(os.getcwd(), "output.txt"), "w")

    Heading = True
    test_case = 1

    #Iterate through the input file
    while True:
        #read input one line at a time
        line = rf.readline()
        line = line.strip()

        if not line:
            #end of file

            #close input file
            rf.close()
            #close output file
            wf.close()
            break
        else:
            #process the line

            if (Heading):
                Heading = False
                NUM_TEST_CASES = int(line)
            else:
                wf.write("Case #" + str(test_case) + ": " + process(line) + "\n")
                test_case += 1
            
main()

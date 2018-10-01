input = "A-large.in"

with open(input, "r") as input_file:
    nb_case = int(input_file.readline())
    for count in xrange(nb_case):
        friends_to_add = 0
        nb_stood_up = 0
        shyness = 0
        max_shy, people = input_file.readline().split()
        max_shy = int(max_shy)
        people = [int(nb) for nb in people]
        for nb in people:
            if nb_stood_up < shyness:
                friends_to_add += 1
                nb_stood_up += 1
            nb_stood_up += nb
            shyness += 1
        print "Case #%d:" %(count+1), friends_to_add

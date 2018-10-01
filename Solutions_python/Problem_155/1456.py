file = open("a_input_large.txt")
out = open('a_output_large.txt', 'w')
T = int(file.readline().strip())
case = 1
for cases in range(T):
    input_line = file.readline().strip().split(" ")
    s_max = int(input_line[0])
    aud_list = [int(i) for i in input_line[1]]

    friends = 0
    s = 0
    while True:
        for index, member in enumerate(aud_list):
            if index <= s:
                s += member
        if sum(aud_list) + friends <= s:
            break
        else:
            friends += 1
            s = friends

    out.write("Case #%i: %i\n" % (case, friends))
    case += 1
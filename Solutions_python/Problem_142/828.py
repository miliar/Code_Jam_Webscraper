import sys,math

cases = int(raw_input())
plays = []

def skeleton(string):
    last_char = string[0]
    skel = last_char
    for char in string[1:]:
        if char != last_char:
            skel += char
        last_char = char

    return skel

def is_possible(strings):
    skel = skeleton(strings[0])
    for string in strings[1:]:
        if skeleton(string) != skel:
            return False
    return True

def mean_length(strings):
    #print strings
    cum = 0
    for string in strings:
        cum += len(string)
    #print cum
    m = float(cum) / len(strings)
    m = int(round(m))
    nearest_to_mean = 0
    for i in range(len(strings)):
        if (len(strings[i])-m)*(len(strings[i])-m) < (len(strings[nearest_to_mean])-m)*(len(strings[nearest_to_mean])-m):
            nearest_to_mean = i

    return nearest_to_mean

def numberLetter(string, letter, group):
    n = 0
    last_char = ''
    curr = -1
    for char in string:
        if last_char != char and char == letter:
            curr+=1
        if char == letter and group == curr:
            n+=1
        last_char = char

    return n

def vass(num):
    if num > 0: return num
    else: return -num

def moves(skeleton,string,target):
    m = 0
    for i in range(len(skeleton)):
        letter = skeleton[i]
        curr = 0
        for j in range(i):
            if skeleton[j] == letter:
                curr+=1
        m += vass(numberLetter(string,letter,curr)- numberLetter(target,letter,curr))
    return m

def target(strings,skel):
    target = ""
    for i in range(len(skel)):
        letter = skel[i]
        curr = 0
        for j in range(i):
            if skel[j] == letter:
                curr+=1
        cum = 0
        for string in strings:
            cum += numberLetter(string,letter,curr)
        num = int(round(float(cum)/len(strings)))
        #print "letter " + letter + " : " + str(num)
        for i in range(num):
            target += letter
    return target

for i in range(cases):
    n_strings = int(raw_input())
    #print answer
    strings = []
    for j in range(n_strings):
        strings.append(raw_input())
    plays.append(strings)

case = 0
for strings in plays:
    case += 1

    sys.stdout.write("Case #"+str(case)+": ")
    #print rows
    if is_possible(strings):
        skel = skeleton(strings[0])
        tg = target(strings,skel)
        #print strings
        #print tg
        tot_moves = 0
        for string in strings:
            tot_moves += moves(skel,string,tg)
        print tot_moves
    else:
        print "Fegla Won";


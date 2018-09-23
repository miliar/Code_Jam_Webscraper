#!/usr/bin/python

f=open('problem_2_small.in', 'r')
output=open('problem_2_small.out', 'w')

cases=int(f.readline())

def parse_solution(stalls, red, orange, yellow, green, blue, violet):
    if orange+green+violet > 0: 
        print "Case #%i: no" % (case+1)
        return ''
    max_unicorns=int(stalls / 2)
    if red <= max_unicorns and blue <= max_unicorns and yellow <= max_unicorns:
        ok=1
    else:
        ok=0
    if ok == 0:
        value="IMPOSSIBLE"
    else:
        ryb=[red, yellow, blue]
        answer=[]
        last=-1
        for i in range(stalls):
            if ryb[0] == ryb[1] and ryb[1] == ryb[2] and i > 0:
                largest=answer[0]
                smallest=(largest + 1) % 3
            elif ryb[0] == ryb[1] and ryb[1] == ryb[2] and i == 0:
                largest=0
                smallest=1
            else:
                largest=ryb.index(max(ryb))
                smallest=ryb.index(min(ryb))
            middle=3 - largest - smallest
            # if case+1 == 5:
            #     print ryb
            #     print largest, middle, smallest
            if last == largest: next_one=middle
            elif last == middle: next_one=largest
            elif ryb[largest] == ryb[middle] and i > 0 and answer[0]==middle:
                next_one=middle
            else: next_one=largest
            answer.append(next_one)
            ryb[next_one] -= 1
            last=next_one
        str_answer=[]
        for x in answer:
            if x == 0: str_answer.append('R')
            if x == 1: str_answer.append('Y')
            if x == 2: str_answer.append('B')
        value=''.join(str_answer)
    # print "Case #%i: %s" % (case+1, value)
    output.write ("Case #%i: %s\n" % (case+1, value))
    # output.write ("Case #%i: %s\n" % (case+1, str(value)))

for case in range(cases):
    arr=f.readline().replace("\n","").split(' ')
    stalls= int(arr[0])
    red=    int(arr[1])
    orange= int(arr[2])
    yellow= int(arr[3])
    green = int(arr[4])
    blue  = int(arr[5])
    violet= int(arr[6])
    parse_solution(stalls, red, orange, yellow, green, blue, violet)

import os
from re import match
def lireinput():
    finput=open('input.txt','r')
    nbrcase=int(finput.readline())
    cases=finput.readlines()
    cases="".join(cases)
    cases=cases.split("\n\n")
    for i in range(nbrcase):
        cases[i]=cases[i].split("\n")

    return (cases)

def resoudre1case(case):
    for y in range(4):
        if (match(("X|T"),case[y][0]) and
        match(("X|T"),case[y][1]) and
        match(("X|T"),case[y][2]) and
        match(("X|T"),case[y][3])) :
            return ("X won")
        if (match(("O|T"),case[y][0]) and
        match(("O|T"),case[y][1]) and
        match(("O|T"),case[y][2]) and
        match(("O|T"),case[y][3])) :
            return ("O won")
    for x in range(4):
        if (match(("X|T"),case[0][x]) and
        match(("X|T"),case[1][x]) and
        match(("X|T"),case[2][x]) and
        match(("X|T"),case[3][x])) :
            return ("X won")
        if (match(("O|T"),case[0][x]) and
         match(("O|T"),case[1][x]) and
         match(("O|T"),case[2][x]) and
         match(("O|T"),case[3][x])) :
            return ("O won")
    if (match(("X|T"),case[0][0]) and
    match(("X|T"),case[1][1]) and
     match(("X|T"),case[2][2]) and
    match(("X|T"),case[3][3])) :
            return ("O won")
    if (match(("O|T"),case[0][0]) and
    match(("O|T"),case[1][1]) and
    match(("O|T"),case[2][2]) and
    match(("O|T"),case[3][3])) :
            return ("O won")
    if (match(("X|T"),case[0][3]) and
    match(("X|T"),case[1][2]) and
    match(("X|T"),case[2][1]) and
    match(("X|T"),case[3][0])) :
            return ("X won")
    if (match(("O|T"),case[0][3]) and
    match(("O|T"),case[1][2]) and
    match(("O|T"),case[2][1]) and
    match(("O|T"),case[3][0])) :
            return ("O won")
    for y in range(4):
        for x in range(4):
            if case[y][x]==".":
                return("Game has not completed")
    return ("Draw")

def ecrireoutput(cases):
    foutput=open("output.txt","w")
    for i in range(len(cases)):
        foutput.write("Case #"+str(i+1)+": "+cases[i]+"\n")

cases=lireinput()
sol=[]
for i in range(len(cases)):
    sol.append(resoudre1case(cases[i]))
ecrireoutput(sol)
    
    
    
            
    


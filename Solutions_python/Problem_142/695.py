from itertools import combinations

def main(input_address):
    input_file = open(input_address, "r")
    solve(input_file, open("D:\\output.txt","w"))

def solve(input_file, output_file):
    cases_number = int(input_file.readline())
    for k in range(cases_number):
        n=int(input_file.readline())
        l=[]
        for i in range(n):
            line = input_file.readline().strip()
            l.append(line)
        answer = compare(l)
        output_file.write("Case #" + 
                          str(k+1) + ": " + answer + "\n")
    input_file.close()
    output_file.close()

def toInt(l):
    for i in range(len(l)):
        l[i] = int(l[i])
    return l

def more(string,i):
    return string[0:i+1] + string[i] + string[i+1:len(string)]
def less(string,i):
    return string[0:i]+string[i+1:len(string)]



def hist(string):
    l = []
    curr = 1;
    for i in range(26):
        l.append([])
    for i in range(1,len(string)):
        if string[i-1] == string[i]:
            curr+=1
        else:
            l[ord(string[i-1])-97].append(curr)
            curr=1
    l[ord(string[len(string)-1])-97].append(curr)
    return l


def basic_compare(str1,str2):
    h1="_"
    h2 = "_"
    for i in str1:
        if i != h1[len(h1)-1]:
            h1+=i
    for i in str2:
        if i != h2[len(h2)-1]:
            h2+=i
    return h1==h2
    

def pair_compare(str1,str2):
    if not basic_compare(str1,str2):
        return -1
    h1 = hist(str1)
    h2 = hist(str2)
    cnt = 0
    for i in range(26):
        for j in range(len(h1[i])):
            cnt+=abs(h1[i][j]-h2[i][j])
    return cnt
            
def compare(l):
    if pair_compare(l[0],l[1])< 0:
        return "Fegla Won"
    else:
        return str(pair_compare(l[0],l[1]))

main("D:\\input.in")
        

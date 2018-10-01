import sys

LS =  4
VN = 10000


def get_ans(sw, inp):
    if sw.count(" ") < 3:
        return 0
    
    return get_number(0, sw, inp)

cache ={}
def get_number(index, string, input):
    if cache.has_key((index, string, input)):
        return cache[(index, string, input)]
    if len(string) > len(input) or index > len(input) -1:
        return 0
    if len(string) == 1:
        return input[index:].count(string)
    s = string[0]
    sum= 0
    for i in range(len(input) - index): 
        si = i+index   
        ip = input[si]
        if s == ip:
            a = get_number(si+1, string[1:], input)
            cache[(si+1, string[1:], input)] = a
           # print si+1, string[1:], a
            sum += a
            sum = sum % VN
            
    return sum








file = "./C-large"
fd = open(file + ".in","r")
pnum = int(fd.readline().strip())
searchw = "welcome to code jam"

case = "Case #No: "
no = 1
output = ""
for i in range(pnum):
    line = fd.readline().strip()
    ans = get_ans(searchw,line)
    
    c = case.replace("No", str(no))
    no += 1
    output += c
    output += ("I am Kento Sato !! Thank you for interesting problems 0000" + str(ans))[-4:] + "\n"  

fd = open(file + ".out", "w")
fd.write(output)
fd.close

    
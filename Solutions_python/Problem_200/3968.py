
import time
def tidy(num, base=0):
    if len(num) == 1:
        if int(num) < base:
            return (-1, "9")
        return (0, num)
    else:
        #if int(num[0]) <= int(num[1]):
        #    return num
        #if num[0] == "1":
        #    return "09"
        if int(num[0]) < base:
            return (-1, "9" * len(num))
        lead = int(num[0])
        next = tidy(num[1:], lead)
        #print 55, next
        if next[0] == -1:
            lead -= 1
            #print base, num
            if lead < base:
                return (-1, "9" * len(num))
        return (0, str(lead) + next[1])
"""       
       x = int(num[0])
        while not x <= int(num[1]):
            x -= 1
        return str(x) + num[1]
    else:
        lead = int(num[0])
        next = tidy(num[1:], lead)
   """     
              
with open("output2.txt", 'w') as f2:
    with open("B-large.in", 'r') as f1:
        f1.readline()
        for i, line in enumerate(f1):
            val = int(tidy(line.strip())[1])
            f2.write("Case #{}: {}\n".format(i+1, val))
print tidy("11114")
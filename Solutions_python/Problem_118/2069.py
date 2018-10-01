import math

def palindrom(n):
    number = str(n)
    palindrom = True
    for i in range(len(number)/2):
        if number[i] is not number[len(number)-i-1]:
            palindrom = False
    return palindrom

f = open('fairsquare', 'r')
x = int(f.readline())
output = ""
for i in range(x):
    fairsquare = 0
    xy = f.readline().split(" ")
    x = int(xy[0])
    y = int(xy[1])
    a = int(round(math.sqrt(x-0.5)))
    b = int(round(math.sqrt(y)))
    for n in range(a,b+1):
        n2 = n*n
        if palindrom(n) and palindrom(n2) and n2 >= x and n2 <= y:
            fairsquare += 1
    output += "Case #"+str(i+1)+": "+str(fairsquare)+"\n"      
      
text_file = open("fairsquareout.txt", "w")
text_file.write(output)
text_file.close()
        
        
        
        
        
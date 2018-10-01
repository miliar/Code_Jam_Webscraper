change = 0
def check(sol,k):
    global change
    
    for i in range(len(sol)):
        #print (sol)
        if sol[i] == "-":
            change = change + 1
            #print (len(sol)-i,k)
            if ((len(sol))-i)>=k:
                for lol in range(k):
                    if sol[lol+i] == '+':
                        sol[lol+i] = '-'
                    else:
                        sol[lol+i]='+'
                check(sol,k)
            else:
               #print ("here ",sol)
               return "IMPOSSIBLE"
    return change        

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
#t = int(input())  # read a line with a single integer
#for i in range(1,t): 
 #   sol, num = input().split(" ")
  #  print (sol , num)
   # k = (int(num))
file_in = open("input.in", "r")
file_out = open("output.txt", "w")
t = int(file_in.readline())
i = 1
for line in file_in:
     sol = ""
     sol, num = line.split(" ")
     print (sol , num)
     k = (int(num))
   
     result = "Case #"+str(i)+": "+str(check(list(sol),k))+"\n"
     i = i+1
     change = 0
     file_out.write(result)
file_out.close()

    #n,m = [int(s) for s in input().split(" ")] 
# read a list of integers, 2 in this case  print("Case #{}: {} {}".format(i, n + m, n * m))  # check out .format's specification for more formatting options
        
print (check(['-','+','-','+'],4))
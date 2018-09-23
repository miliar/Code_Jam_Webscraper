import math

def solve_c(path="E:\\Users\\Neta\\Desktop\\dashyts\\googlejam.txt"):
    f = open(path, "r")
    T = f.readline()
    T = int(T)
    #path_out = "E:\\Users\\Neta\\Desktop\\dashyts\\googlejamSOL.txt"
    #fout = open(path_out, "w")
    case = 0
    for i in range(T):
        line = f.readline()
        case = case + 1
        args = line.split(" ")
        N = int(args[0])
        K = int(args[1])
        log2k = math.log2(K)
        #print("log2k is: " + str(log2k))
        floorlog2k = math.floor(log2k)
        #print("floorlog2k is: " + str(floorlog2k))
        down = 2**floorlog2k
        #print("down is: " + str(down))
        up = N+1 -K
        #print("up: "+str(up))
        midanswer = math.ceil(up/down)
        #print("midanswer is: "+ str(midanswer))
        finalanswer = (midanswer - 1)
        if finalanswer %2 == 0:
            print("Case #" + str(case) +": "+ str(int(finalanswer/2))+" "+str(int(finalanswer/2)))
        else:
            print("Case #" + str(case) +": "+ str(int(finalanswer/2)+1)+" "+str(int(finalanswer/2)))
        
        
        

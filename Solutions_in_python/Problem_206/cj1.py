
import sys
sys.setrecursionlimit(10000)
def read_one_input(f):

    s=f.readline().strip("\n").split()
    d=int(s[0])
    n=int(s[1])
    horses=[]
    for i in range (n):
        s=f.readline().strip("\n").split()
        horse=[]
        horse.append(int(s[0]))
        horse.append(int(s[1]))
        horses.append(horse)
    horses.append([d,0])
    return horses

def time_to_reach(horses):
    if len(horses)==1:
        return 0
    d=horses[-1][0]

    return max(float(d-horses[0][0])/horses[0][1], time_to_reach(horses[1:]))

def main():
    file_name="A-large"
    input_file=file_name+".in"
    output_file=file_name+".out"
    f=open(input_file,"r")
    f2=open(output_file,"w")
    t=int(f.readline().strip("\n"))
    for i in range(t):
        horses=read_one_input(f)
        r=time_to_reach(horses)

        d=horses[-1][0]
        f2.write("Case #"+str(i+1)+": "+str(float(d)/r)+"\n")
    f.close()
    f2.close()

if __name__=="__main__":
    main()





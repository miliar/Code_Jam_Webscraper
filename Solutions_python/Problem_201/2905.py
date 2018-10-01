## Returns the number of empty stalls
## between i and j with j > i
def distance(i, j):
    return abs(j - i - 1)

## Returns the place where i should be in l
## l is a sorted list
def search(l, i):
    j = 0
    while(l[j] < i):
        j += 1
    return j

## Adds in stalls the stall chosen by a person
## who enters the bathroom when its state is
## as described in stalls, returns Ls and Rs
## for this stall
def stall_chosen(stalls, N):
    Ls = -1
    Rs = -1
    stall_chosen = -1
    l = len(stalls)

    ## Looking for stall_chosen
    for i in range (l - 1):
        if(stalls[i + 1] - stalls[i] > 1):
            cur_mid = (stalls[i] + stalls[i + 1]) //2
            if((min(distance(stalls[i],cur_mid), distance(cur_mid, stalls[i + 1])) > min(Ls, Rs))):
                    Ls = distance(stalls[i],cur_mid)
                    Rs = distance(cur_mid, stalls[i+1])
                    stall_chosen = cur_mid
            elif(min(distance(stalls[i],cur_mid), distance(cur_mid, stalls[i + 1])) == min(Ls, Rs)):
                    if(max(distance(stalls[i],cur_mid), distance(cur_mid, stalls[i + 1])) > max(Ls,Rs)):
                        Ls = distance(stalls[i],cur_mid)
                        Rs = distance(cur_mid, stalls[i+1])
                        stall_chosen = cur_mid
                    
    ## Adding stall_chosen in stalls
    l = len(stalls)
    stalls.insert(search(stalls, stall_chosen), stall_chosen)
            
    return (Ls, Rs)

def stall_chosen_by_last(N, K):

    stalls = [0, N + 1]

    for i in range(K - 1):
        stall_chosen(stalls, N)
    (Ls,Rs) = stall_chosen(stalls, N)
    
    return (max(Ls,Rs), min(Ls,Rs))

def main():
    file = open(r'C-small-1-attempt2.in', 'r')
    lines = file.readlines()
    file.close()

    n = int(lines[0])

    output = []

    for i in range(1, n + 1):
        space = 0
        
        while(lines[i][space] != ' '):
            space += 1
            
        N,K = int(lines[i][:space]), int(lines[i][space + 1:])
        x,y = stall_chosen_by_last(N,K)
        
        output += ["Case #" + str(i) + ": " + str(x) + " " + str(y) + "\n"]
                   
    file= open(r'ProblemC_output.txt', 'w')
    file.writelines(output)
    file.close()

main()

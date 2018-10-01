def main():
    inFile = open('largein.txt', 'r')
    outFile = open('largeout.txt', 'wb')
    
    count = 1
    case = 1
       
    for line in inFile:
        if count == 1:
            count = 0
            continue
        else:
            man = 0
            m, n = line.split(" ")
            m = int(m)
            num = list(n)[:len(list(n))-1]
            dig = [int(i) for i in num]
            for i in range(len(dig)):
                if sum(dig[:i]) < i:
                    dig[i] += 1
                    man += 1 
            outFile.write("case #{}".format(case)+ ": " + str(man)+"\n")
            case += 1        
            
    
if __name__ == "__main__" :main()
T = int(input())
for case in range(T):
    line = input()
    N = int(line.split(" ")[0])
    R = int(line.split(" ")[1]) 
    O = int(line.split(" ")[2]) 
    Y = int(line.split(" ")[3]) 
    G = int(line.split(" ")[4])
    B = int(line.split(" ")[5]) 
    V = int(line.split(" ")[6]) 
    impossible = False
    
    if ((O > B ) or (G > R) or (V > Y) or (R > (B+Y+G)) or (Y > (R+B+V)) or (B > (R+Y+O))):
        impossible = True
    
    if (not impossible):
        stable = ""
        possible = ["R","O","Y","G","B","V"]
        for horse in range(N):
            if(O > 0 and "O" in possible):
                stable += "O"
                O -= 1
                possible = ["B"]
                continue
            if(G > 0 and "G" in possible):
                stable += "G"
                G -= 1
                possible = ["R"]
                continue
            if(V > 0 and "V" in possible):
                stable += "V"
                V -= 1
                possible = ["Y"]
                continue
            if(R > 0 and "R" in possible):
                stable += "R"
                R -= 1
                if (B > Y):
                    if (B > G):
                        possible = ["B"]
                    else:
                        possible = ["G"]
                else:
                    if (Y > G):
                        possible = ["Y"]
                    else:
                        possible = ["G"]
                continue
            if(B > 0 and "B" in possible):
                stable += "B"
                B -= 1
                if (R > Y):
                    if (R > O):
                        possible = ["R"]
                    else:
                        possible = ["O"]
                else:
                    if (Y > O):
                        possible = ["Y"]
                    else:
                        possible = ["0"]
                continue
            if(Y > 0 and "Y" in possible):
                stable += "Y"
                Y -= 1
                if (B > R):
                    if (B > V):
                        possible = ["B"]
                    else:
                        possible = ["V"]
                else:
                    if (R > V):
                        possible = ["R"]
                    else:
                        possible = ["V"]
                continue
            impossible = True
            break
        
    if (impossible):
        print("Case #{}: IMPOSSIBLE".format(case+1))
    else:
        print("Case #{}: {}".format(case+1, stable))



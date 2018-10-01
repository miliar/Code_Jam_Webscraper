def solve(flip_number , string_tobe_flipped,flipping,flips):
    d = {"+" : "-","-" : "+"}
    #print(string_tobe_flipped,flips)
    #print(flipping,string_tobe_flipped)
    #print("+" * (len(string_tobe_flipped)))
    if string_tobe_flipped == list("+" * (len(string_tobe_flipped))):
        #print("hhhhhhhhhhhhhhhhhhhh")
        return(flips)
    elif flipping > len(string_tobe_flipped)-flip_number:
        return "IMPOSSIBLE"
    else:
        #print(flips)
        a = list(string_tobe_flipped)
        for value2 in range(flipping,flipping + flip_number):
            a[value2] = d[a[value2]]
        c = solve(flip_number,a,flipping + 1,flips+1)
        e = solve(flip_number,string_tobe_flipped,flipping + 1,flips)
        if c == "IMPOSSIBLE"and d == "IMPOSSIBLE":
            return("IMPOSSIBLE")
        elif c == "IMPOSSIBLE":
            return(e)
        else:
            return(c)

a = int(input())
for value in range(1,a+1):
    b = input().split()
    b[0] = list(b[0])
    b[1] = int(b[1])
    print("Case #"+ str(value) + ":",(solve(b[1],b[0],0,0)))

        

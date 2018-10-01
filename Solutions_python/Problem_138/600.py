def war(ken, naomi, N):
    score = 0
    for block1 in naomi:
        for block2 in ken:
            if block1 > block2:
                score += 1
                ken.pop()
                break
            else:
                ken.remove(block2)
                break
    return str(score)
def dec_war(ken, naomi, N):
    j = N - 1
    while j >= 0:
        if naomi[j] < ken [j]:
            ken.remove(ken[0])
            naomi.pop()
        j -= 1
    return str(len(naomi))   
file1 = open("D-large.in","r")
file2 = open("output","w")
T = int(file1.readline())
i = 1
while i <= T:
    N = int(file1.readline())
    naomi = file1.readline().split()
    ken = file1.readline().split()
    naomi.sort(reverse = 1)
    ken.sort(reverse = 1)
    file2.write("Case #"+str(i)+": "+dec_war(ken[:],naomi[:],N)+" "+war(ken[:], naomi[:],N)+"\n")
    i += 1

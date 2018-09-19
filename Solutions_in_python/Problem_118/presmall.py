psq = []
limit = 10**7 + 1
for i in range(limit):
    istr = str(i)
    if istr[::-1] == istr:
        j = i*i
        jstr = str(j)
        if jstr[::-1] == jstr:
            psq.append(j)

print(psq)


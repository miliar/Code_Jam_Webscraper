''' Solution from text:

30	10 10 10		10		always 10
29	9 10 10			10		always 10
28	9 9 10	8 10 10*	10		always 10
27	9 9 9	8 9 10*		9	10*	10 else 9
26	8 9 9	8 8 10*		9	10*	10 else 9
25	8 8 9	7 9 9*		9		always 9
24	8 8 8	7 8 9*		8	9*	9 else 8
23	7 8 8	7 7 9*		8	9*	9 else 8
22	7 7 8	6 8 8*		8		always 8
21	7 7 7	6 7 8*		7	8*	8 else 7
20	6 7 7	6 6 8*		7	8*	8 else 7
19	6 6 7	5 7 7*		7		always 7
18	6 6 6	5 6 7*		6	7*	7 else 6
17	5 6 6	5 5 7*		6	7*	7 else 6
16	5 5 6	4 6 6*		6		always 6
15	5 5 5	4 5 6*		5	6*	6 else 5
14	4 5 5	4 4 6*		5	6*	6 else 5
13	4 4 5	3 5 5*		5		always 5
12	4 4 4	3 4 5*		4	5*	5 else 4
11	3 4 4	3 3 5*		4	5*	5 else 4
10	3 3 4	2 4 4*		4		always 4
9	3 3 3	2 3 4*		3	4*	4 else 3
8	2 3 3	2 2 4*		3	4*	4 else 3
7	2 2 3	1 3 3*		3		always 3
6	2 2 2	1 2 3*		2	3*	3 else 2
5	1 2 2	1 1 3*		2	3*	3 else 2
4	1 1 2	0 2 2*		2		always 2
3	1 1 1	0 1 2*		1	2*	2 else 1
2	0 1 1	0 0 2*		1	2*	2 else 1
1	0 0 1			1		always 1
0	0 0 0			0		always 0

Soultion:
(1) Sort values high to low
(2) 1, 4, 7, 10, 13, 16, 19, 22, 25, 28 + 0, 29, 30 --> always
others (27/26, 24/23, ...) are _ else _
if n % 3 == 1: score is (n+2)/3
elif n == 0: score is 0
elif n in [29,30]: score is 10
else:
if n % 3 == 2: n+= 1
score = n / 3
if surprise > 0 and score = pval - 1: score += 1, then surprise -= 1
(3) filter scores by min, then length

'''

def dancing(st):
    if st[-1] == "\n":
        st = st[:-1]
    vals = [int(x) for x in st.split(" ")]
    n = vals[0]
    surprises = vals[1]
    pval = vals[2]
    vals = vals[3:]
    if n != len(vals):
        raise ValueError
    vals.sort(reverse=True)
    scores = []
    for val in vals:
        score = 0
        if val % 3 == 1:
            score = (val + 2) / 3
        elif val == 0:
            score = 0
        elif val in [29,30]:
            score = 10
        else:
            if val % 3 == 2:
                val += 1
            score = val / 3
            if surprises > 0 and score == (pval - 1):
                score += 1
                surprises -= 1
        scores.append(score)
    goodscores = filter(lambda sco: sco >= pval, scores)
    answer = len(goodscores)
    
    return str(answer)

def main(filein):
    f = open(filein, "r")
    outname = filein.split(".")[0] + "OUT.txt"
    g = open(outname, "w")

    count = -1
    for line in f:
        count += 1
        if count == 0:
            continue
        newline = "Case #" + str(count) + ": " + dancing(line) + "\n"
        g.write(newline)
    
    f.close()
    g.close()
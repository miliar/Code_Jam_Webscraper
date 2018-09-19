infile = open('A-small-attempt2.in', 'r')
try:
    outfile = open('A-small.out', 'w')
except:
    outfile = open('A-small.out', 'x')
st = infile.readline()
st = st.rstrip()
n = int(st)
for p in range(0, n):
    st = infile.readline()
    st = st.rstrip()
    x = int(st)
    first = []
    for i in range(0, 4):
        st = infile.readline()
        st = st.rstrip()
        if (i+1) == x:
            sp = st.split(' ')
            for spp in sp:
                first.append(int(spp))
    st = infile.readline()
    st = st.rstrip()
    x = int(st)
    second = []
    for i in range(0, 4):
        st = infile.readline()
        st = st.rstrip()
        if (i+1) == x:
            sp = st.split(' ')
            for spp in sp:
                second.append(int(spp))
    count = 0
    m = 0
    for i in range(0, 4):
        count += second.count(first[i])
        if first[i] in second:
            m = i
    outfile.write('Case #' + str(p+1) + ': ')
    if count == 0:
        outfile.write('Volunteer cheated!\n')
    if count == 1:
        outfile.write(str(first[m]) + '\n')
    if count > 1:
        outfile.write('Bad magician!\n')
infile.close()
outfile.close()

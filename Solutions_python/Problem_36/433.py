matches = 0
subseq = "welcome to code jam"
texts = []

def find_subseq(subseq, text, ssindex, txtindex):
    global matches
    if ssindex == len(subseq) - 1:
        matches += 1 % 10000
    else:
        txtindex += 1
        while txtindex < len(text):
            if subseq[ssindex + 1] == text[txtindex]:
                find_subseq(subseq, text, ssindex + 1, txtindex)
            txtindex += 1

N = input()
for i in range(N):
    texts.append(raw_input())
for i in range(len(texts)):
    find_subseq(subseq, texts[i], -1, -1)
    print "Case #%d: %04d" % (i + 1, matches)
    matches = 0

ciphertext = "yeq" + \
"ejp mysljylc kd kxveddknmc re jsicpdrysi" + \
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" + \
"de kr kd eoya kw aej tysr re ujdr lkgc jv"

plaintext = "aoz" + \
"our language is impossible to understand" + \
"there are twenty six factorial possibilities" + \
"so it is okay if you want to just give up"

cipher = {}

alphabet = "abcdefghijklmnopqrstuvwxyz"

for cipherchar, plainchar in zip(ciphertext, plaintext):
    if cipherchar not in alphabet:
        continue
    if cipherchar in cipher:
        assert cipher[cipherchar] == plainchar
    else:
        assert plainchar not in cipher.values()
        cipher[cipherchar] = plainchar

if len(cipher) == len(alphabet)-1:
    unused_cipherchars = list(alphabet)
    unused_plainchars = list(alphabet)
    for cipherchar, plainchar in cipher.items():
        unused_cipherchars.remove(cipherchar)
        unused_plainchars.remove(plainchar)
    assert len(unused_plainchars) == 1
    assert len(unused_cipherchars) == 1
    assert unused_cipherchars[0] not in cipher.keys()
    assert unused_plainchars[0] not in cipher.values()
    cipher[unused_cipherchars[0]] = unused_plainchars[0]

print len(cipher)
print cipher

def decode(ciphertext):
    global cipher
    plaintext = ""
    for k in ciphertext:
        if k in cipher:
            plaintext += cipher[k]
        else:
            plaintext += k
    return plaintext

infile = open("a-small-attempt0.in", "r")
outfile = open("a-small-attempt0.out", "w")

T = int(infile.readline())
for casenum in range(1, T+1):
    ciphertext = infile.readline().strip()
    outfile.write("Case #%d: %s\n" % (casenum, decode(ciphertext)))

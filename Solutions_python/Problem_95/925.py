raw_alphabet = "yhesocvxduiglbkrztnwjpfmaq"

alphabet = {}

for i in xrange(len(raw_alphabet)):
    alphabet[chr(ord('a') + i)] = raw_alphabet[i]


def decrypt(text):
    output = ""
    for c in text:
        if alphabet.has_key(c):
            output += alphabet[c]
        elif c != "\n":
            output += c
    return output

fin =  open("tongues.txt", "r")

fin = fin.readlines()

inputs = int(fin[0])

fin.pop(0)

for i in xrange(inputs):
    output = decrypt(fin[i])
    print ("Case #%d: " % (i+1)) + output



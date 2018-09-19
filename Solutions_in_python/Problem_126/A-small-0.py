import string

consonants = frozenset(set(string.ascii_lowercase) - set(["a", "e", "i", "o", "u"]))
print consonants

def reader(inFile):
    name, n = inFile.getWords()
    n = int(n)
    return (name, n)


def solver(stuff):
    name, n = stuff
    num_of = 0
    for i in range(len(name)):
        for j in range(i+1, len(name) + 1):
            if j-i < n:
                continue
            sub_name = name[i:j]
            #print sub_name
            if len(sub_name) == n and set(sub_name).issubset(consonants):
                #print "##subset", len(name)-(j)+1
                num_of += len(name)-j+1
                break
            elif set(sub_name[-n:]).issubset(consonants):
                #print "##subset zadi", len(name)-(j)+1
                num_of += len(name)-j+1
                break
    #print name
    #print name.translate("A", "".join(consonants))
    #print n
    return num_of


if __name__ == "__main__":
    from GCJ import GCJ
    GCJ(reader, solver,
        "/home/mabu/gcj/cj131C", "A").run()

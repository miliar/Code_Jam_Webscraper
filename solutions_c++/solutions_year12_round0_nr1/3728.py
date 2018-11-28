i = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv"
o = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"

d = { 'y' : 'a', 'e' : 'o', 'q' : 'z', 'z' : 'q' }

for ci, co in zip(i, o):
    d[ci] = co

for k in d:
    print "d['%s'] = '%s';" % (k, d[k])



###################################################################
#
#   Google Code Jam - 2015 Q A
#
################################################################### 

class GrabData(object):
    """
    Reads the file specified, and splits it up into the relevant information.
    """

    def __init__(self,data):
        self._data = []
        self._shyness = []
        for line in data:
            self._data.append(line.strip())
                
    def parseData(self):
        for x in self._data[1:]:
            audience = list(enumerate([int(i) for i in list(x.split()[1])]))
            self._shyness.append(audience)

    def getAudience(self):
        return self._shyness
                

class Main(object):

    def __init__(self,filein, fileout):
        self._input = open(filein)
        data = GrabData(self._input)
        data.parseData()
        self._audience = data.getAudience()

        f = open(fileout,"w+")

        for x, y in enumerate(self._audience,1):
            if len(y) > 1:
                st = 0
                num_added = 0
                last_added = 0
                for s_level in y:
                    st += s_level[1]
                    try:
                        if st == y[s_level[0]+1][0]:
                            continue
                        else:
                            while st < y[s_level[0]+1][0]:
                                last_added = x
                                st += 1
                                num_added += 1
                    except IndexError:
                        f.write("Case #{0}: {1}\n".format(x, num_added))
            else:
                f.write("Case #{0}: {1}\n".format(x, 0))

        self._input.close()
        f.close()

main = Main("A-large.in","A-large.out")




VACANT = 0
OCCUPIED = 1

class Pooper:
    def findMinMaxForPooping(self, input):

        numStalls = int(input.split(' ')[0])
        numPoopers = int(input.split(' ')[1])

        stalls = [VACANT] * (numStalls + 2)
        stalls[0] = OCCUPIED
        stalls[len(stalls)-1] = OCCUPIED

        while (numPoopers != 1):
            nextStall = self.stallForNextPooper(stalls)
            stalls[nextStall] = OCCUPIED
            numPoopers -= 1

        nextStall = self.stallForNextPooper(stalls)
        ls,rs = self.getLR(stalls,nextStall)

        if ls >= rs:
            return ls, rs
        return rs, ls


    def stallForNextPooper(self, stalls):

        # Build list of max min
        maxMinGlobal = -9999
        pStalls = []
        for index in range (len(stalls)):
            if (stalls[index] == VACANT):
                ls,rs = self.getLR(stalls, index)

                maxMin = self.minS(ls, rs)
                if maxMin > maxMinGlobal:
                    maxMinGlobal = maxMin
                    pStalls[:] = []
                    pStalls.append(index)
                elif maxMin == maxMinGlobal:
                    pStalls.append(index)

        if len(pStalls) == 1:
            return pStalls[0]


        # Build list of max max - Find the max - remove all that does not have that max
        maxMaxGlobal = -9999
        for index in range(len(pStalls)):
            ls, rs = self.getLR(stalls, pStalls[index])
            maxMax = self.maxS(ls,rs)
            if maxMax > maxMaxGlobal:
                maxMaxGlobal = maxMax

        index = 0
        while index < len(pStalls):
            ls, rs = self.getLR(stalls, pStalls[index])
            maxMax = self.maxS(ls,rs)

            if maxMax != maxMaxGlobal:
                pStalls.pop(index)
            else:
                index += 1

        if len(pStalls) == 1:
            return pStalls[0]

        return pStalls[0]

    def getLR(self, stalls, index):
        ls,rs = 0,0

        i = index
        while (i >= 0 and stalls[i-1] == VACANT):
            ls += 1
            i -= 1

        i = index
        while (i < (len(stalls)-1) and stalls[i+1] == VACANT):
            rs += 1
            i += 1

        return (ls, rs)

    def minS(self, ls, rs):
        if ls <= rs:
            return ls
        return rs
    def maxS(self, ls, rs):
        if ls >= rs:
            return ls
        return rs



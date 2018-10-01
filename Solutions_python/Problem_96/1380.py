'''
Created on Apr 13, 2012

@author: Irving
'''

class dancers(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.file = open('C:\Users\Irving\Downloads\B-large.in', 'r')
        self.output = open('C:\Users\Irving\Desktop\output.in', 'w')
    
    def maxScorers(self):
        first = True
        case = 1
        for line in self.file:
            if first:
                first = False
            else:               
                sentence = "Case #" + str(case) + ": "
                line = line.rstrip()
                data = line.split(" ")
                triples = int(data[1])
                maxScore = int(data[2])
                scores = data[3:]
                maxDancers = 0
                triplesCount = 0
                for score in scores:
                    dancerScores = []
                    dancerScores.insert(0,int(score)/3)
                    dancerScores.insert(1,(int(score) - dancerScores[0])/2)
                    dancerScores.insert(2,int(score) - (dancerScores[0] + dancerScores[1]))
                    if max(dancerScores) >= maxScore:
                        maxDancers = maxDancers + 1
                    elif (max(dancerScores) == min(dancerScores) and 
                            (maxScore - max(dancerScores)) == 1 and 
                            max(dancerScores) != 0 and triplesCount < triples):
                        maxDancers = maxDancers + 1
                        triplesCount = triplesCount + 1
                    elif ((dancerScores.count(max(dancerScores))) == 2 and triplesCount < triples and
                          (maxScore - max(dancerScores)) == 1):
                        triplesCount = triplesCount + 1
                        maxDancers = maxDancers + 1
                sentence = sentence + str(maxDancers) + "\n"
                case = case + 1
                self.output.write(sentence)
        self.output.close()
    
if __name__ == "__main__":
    dancer = dancers()
    dancer.maxScorers()    
                        
                    
                        
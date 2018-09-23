'''
Created on 8 avr. 2017

@author: franc
'''
import sys
from src.Loader import Loader
from src.PancakePile import PancakePile
from src.Pancake import Pancake

if __name__ == '__main__':
    loader = Loader(sys.argv[1])
    data = loader.returnDataArray()
    nb = data["NB"]
    del data["NB"]
    out = {}
    for case in data.keys():
        pile = PancakePile(int(data[case][1]))
        for c in str(data[case][0]):
            pile.addPancake(Pancake(c))
        out[case]=pile.solve()
        #print ("Case: " + str(out[case]))
    
    for key in out.keys():
        print (key + str(out[key]))
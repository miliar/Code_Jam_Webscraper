# -*- coding: utf-8 -*-

from util import *

# Constants

NORTH = AddableTuple((-1,0))
WEST = AddableTuple((0,-1))
EAST = AddableTuple((0,1))
SOUTH = AddableTuple((1,0))

CARDINAL_POINTS_PRIORITY = [NORTH, WEST, EAST, SOUTH]

class Land(object):
    availableSinkNames = None
    land = list()
    hw = None # Height / Width
    
    @classmethod
    def createFromGCJExerciseFile(cls, fileHandle):
        height, width = [int(a) for a in fileHandle.readline().strip().split(" ")]
        
        result = list()
        for i in range(0, height):
            sublist = list()
            values = fileHandle.readline().strip().split(" ")
            
            for value in values:
                sublist.append(value)
            
            if(len(sublist) != width):
                raise ValueError("Values qty must be equal to width")
            
            result.append(sublist)
        
        return cls((height, width), result)
    
    def __init__(self, hw, values):
        """I owe you data validation :)"""
        regionedValues = list()
        
        for x in range(0, hw[0]):
            sublist = list()
            for y in range(0, hw[1]):
                sublist.append(Region(self, (x,y), values[x][y]))
            regionedValues.append(sublist)
        
        self.availableSinkNames = list("abcdefghijklmnopqrstuvwxyz")
        self.land = regionedValues
        self.hw = hw
    
    def getFromXY(self, xy):
        if (xy[0] < 0 or xy[0] >= self.hw[0]) or (xy[1] < 0 or xy[1] >= self.hw[1]):
            raise IndexError("Out of index")
        
        return self.land[xy[0]][xy[1]]



class Region(object):
    parentLand = None
    altitude = None
    xy = None
    _sinkName = None
    
    def __init__(self, parentLand, xy, altitude):
        self.parentLand = parentLand
        self.xy = AddableTuple(xy)
        self.altitude = altitude
    
    #@cacheDecorator
    def getMaxNearRegion(self):
        maxNearRegion = None
        
        for cardinalOffset in CARDINAL_POINTS_PRIORITY:
            try:
                nearRegion = self.parentLand.getFromXY(self.xy + cardinalOffset)
                if nearRegion.altitude < self.altitude:
                    if maxNearRegion == None or maxNearRegion.altitude > nearRegion.altitude:
                        maxNearRegion = nearRegion
            except IndexError:
                pass
        
        return maxNearRegion
    
    #@cacheDecorator
    def isSink(self):
        return self.getMaxNearRegion() == None
        
    def getSinkName(self):
        if self.isSink():
            if self._sinkName == None:
                self._sinkName = self.parentLand.availableSinkNames[0]
                del self.parentLand.availableSinkNames[0]
        
            return self._sinkName
        else:
            raise ValueError("I'm not a sink :( sorry")
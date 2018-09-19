

'''
extremes.py

This module was written in 2004 by Josiah Carlson and has been placed in the
public domain.

This module implements the functionality described in PEP 326
http://www.python.org/peps/pep-0326.html


Standard usage:

import extremes
from extremes import UniversalMaximum, UniversalMinimum
from extremes import uMax, uMin
etc.

UniversalMaximum > k  # -> True for all k != UniversalMaximum
UniversalMinimum < k  # -> True for all k != UniversalMinimum

While the standard names for these objects is UniversalMaximum and
UniversalMinimum, the aliases uMax and uMin have been included for those who
want/need shorter names.
'''

class ExtremeType(object):
    '''
    Base type for all extreme values.
    '''
    def __new__(cls, cmpr, rep, *args, **kwds):
        if cmpr is -1:
            it = cls.__dict__.get('__UniversalMinimum__')
            if it is not None:
                return it
            cls.__UniversalMinimum__ = it = object.__new__(cls)
        elif cmpr is 1:
            it = cls.__dict__.get('__UniversalMaximum__')
            if it is not None:
                return it
            cls.__UniversalMaximum__ = it = object.__new__(cls)
        else:
            raise TypeError("first argument must be either -1 or 1")
        assert type(rep) is str
        it.__comparison = cmpr
        it.__repr = rep
        return it

    def getcomparison(self):
        return self.__comparison

    def __cmp__(self, other):
        if isinstance(other, ExtremeType):
           return cmp(self.__comparison, other.getcomparison())
        return self.__comparison

    def __repr__(self):
        return self.__repr

    def __add__(self, other):
        if self.__comparison == 1:
            return self
        return NotImplemented
    __radd__ = __add__

    def __sub__(self, other):
        if self.__comparison == -1:
            return self
        return NotImplemented

uMax = UniversalMaximum = ExtremeType(1, 'UniversalMaximum')
uMin = UniversalMinimum = ExtremeType(-1, 'UniversalMinimum')

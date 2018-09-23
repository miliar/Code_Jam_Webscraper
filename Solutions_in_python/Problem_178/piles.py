def isHappy(pile):
    for i in pile:
        if i != "+":
            return False
    return True

def flipTo(pile, upTo):
    if pile[0]=="+":
        return "-"*upTo+pile[upTo:]
    else:
        return "+"*upTo+pile[upTo:]

def flippy(pile):
    if isHappy(pile):
        return 0
    startsNeg = (pile[0]=='-')
    count = 0
    while not isHappy(pile):
        if startsNeg:
            upTo = pile.find('+')
            if upTo>=0:
                pile= flipTo(pile, upTo)
                startsNeg= not startsNeg
            else:
                return count+1
        else:
            upTo = pile.find('-')
            pile= flipTo(pile, upTo)
            startsNeg= not startsNeg
        count += 1
    return count

things = """-
-+
+-
+++
--+-
+---+++--+-+----+++----++-+---+-+-++++-++-+-+++++---+++++---+--+-----++-+-++-++++-+-+-+-+++---+--+-+
--------------------------------------------------
--+
-+---++--+-----+---++--++--++-+-+++--++-+++-+--++-++++++++-++++++++++--+-+--++-+--++---+++++-++---+-
++---+++-+++---+-+-++-+----+-+++-+---
-+-+--+++++--+-+-+-+--+-+-+++--++---+-++---++---+++++----+-+++++++--++--+---+++--++-+-++++-+-++-----
-++
-++--+-++-+-++-+++-++-+++-+++-+-+--++--+----+-+-+-+---+-+++++---+----+-+++--+---+--++++-++-++--++-++
+-+-++---++-----++-++---++++++----++-+-----++--+---+------+--++--++-++
-+--++-+-+-+--+--+--++----------++--+---+-++-+-+++---++-+----+-+----+++-+--+---+----+----+------+--+
+-+++----+++++-++-+++++----+-++-++-+----+
--+-----------+-++--+-+--++--+-++-+-++-+--++++++++----+-++-+-+----+-+--+++++-++-+-+++-+++-----+-+-++
-+-++--++-++-+--+--++-+-------+++---++++++++++--+--++++++---++-++-++--+---+++-+++++-+++++-+--+++-+++
++++-----+--++++--++-----+-+++-+-++-+++++++----+++-++---+++++----+---+---++++++-++--+-+---++++------
-+++--+++++++-++-+-+------+++++-+++--++--+-++----++-++-+-+-----+---
---+--+++---+-++-++-+-+--+++--+-+-+-----++---+++--+--+----+++-++-++++-++-----++---+--+-++-+--+--+--+
---++---+------++++---+---++++-++-+--++-++-+-+-+++---+-+++-+++++-+---+++++-+--+-++-+-+----+-+-++++++
+-+----+-+++++-++++-++----+-+-+++---++--++++--+-++---++++--+-+-----+-++++---+-++--------+-+---
--+-+-----+++-+-+-+++--++---++---+-++++++-+--++-+++-+-+--+++--+-+-+-++-+---+++++++++-++++---+-++-+-+
--+++--+-+-+---+-+++----+--+++-++----+--++-++-+-+-+++++-++++-++---+-+-----++-+----+-+---+++--+---+--
+--
++-+++--++++-++--+------++++---+---+++++--+-+--++++-++-+-++--++++-+-++-+---+---+--+--+--+++++-------
--++--+++-+-----+++-+--+++-+---++-----++--+---++++----+--------+-+++++-+++++++++-+-+-++--+-+++----++
+--+---++-++----+-++-++--+++-+++-+++------+---++-----+
-+-++-+-+++-++-++--+--++-+-++-+-+-+--++--+-++++--+++---++-+--+-----++-++-++++++--+---+-+-+--+----+-+
++++--+-+++-+-+---++---+-+--++++++++
+--------------------------------------------------------------------------------------------------+
+--------+
++--+-------++--+--++--+++----------+--+-+-++-----+++++++---+-------+-+++++-+++--+-+-+----++++--++--
--+-+---++-+-+-+--+--++++--+-++-+-+-+-++++++-----+-++--+--+--++-+-----+------+++-----+++++++++++-+-+
+-++---+-+-+++++--+-----+---+++--++++-+---+-+-----+++---+-+++-+-+--++++-+-++-
++-+++--++-++--+----++-+---++--++-++--+++---+--+++-+----+-++--+-+--++---+-------++++-+-++-++++-++-+-
+-++---+-+-++-+++-+-+----+--+++-++--+--------+-+--++--+-+-+-+++--+--+++-+---++++++--+-++--+++-+---+-
+++++-+-+-++--+---+-+--+-++-+-++--++-+++-+--++++++--+---++--++--+--+-++-++--+-+--+---++-++-+++-++++-
++-+++-+---++----+++-+---++-+--+++++++--+++----+----+---+-+-+-+--+---++++----+----+-+----+-+--+++++-
-----
---+++-----+++-+++++--+-+-+----+-++--------+-+-++++---++-++++++++---++-+--+++---+-++++++-----+++++--
++++++++++++++++++++++++++++++++++++++++++++++++++
+---+----+--+-+++--+--++-+----+-+--+-++-+-+--+--++-+++----++-++--+++---+-++-++-+--+-+++--++++-+
-++--+--++++--++-+-++++--+-+--+-+-+----+-+-+---+++--++-+++-+-+-+++--------+++---------+-+-++++++++--
+++----++-+---+--+-++++-++-----++-++-++++++-+-+-+++-+-++-+----+++++++++++---++--+---+-+-+-+--++-+++-
+++--++-+------++++---+---+-+----++------+-------+--++---+++-+--+-+-+-+--+---+-+++++++-+----+-------
+++++
++-++++++-++++-++--+++------++-+--++-+-+++-++------+-
-+-+++-+-+++-+-++++++-+-+-+-+--+--++--+-++--++----++--+++-++--+--++--+++--++-++--+-----+----+-++----
--
-++---++++-++++-+++-++-+----+++-+++-+-+----+---+---+++---+------+-+------+-++++++--+-+-++--+-+-+++-+
+--++-+++-+----+-+--+++---++-+-----+++++--+++-+-+-++-------++---+-+----+-+--++-++-+++++--++-++++-+-+
--+-+++-+-++-+++----+-++-++-+----++--+--+-+---++-+--+++++--+-+++++-+++++-+-++--+--++--++--+++++---++
+-+-+--++-+--+--++---+--+--++++++-++-+--+-++++++---+++--++-+---+--+---+-++-++-----++--++---+-+++-+-+
----+-------++++-+--++++++-+--
++-++-+--+++-++-+++-+-++++---------+------++-+-+++--++-++-++-+++++-+++++-+-++-+--+---++----+++-+-+++
---+---+-+-+-++++--+++--++------+--++-+
-+-+-+++-++-------++-+--++----++--+-+++--------+-++++++----+-+-+-+-+--+++++++-+----++++++++-+-+-++-+
--+----++-+-+-+-+-+++---+++----+--+-++-++--+--+-+-+---+++--+++---+++---+++----+---+--++--+-++++++-+-
--++------++-++-+---++++---+-+++-----++++---+--+++++-+-+-++-+-+++-++-+++-+----+---+-+-+---+--++++-++
-+-+++++++-++--+---++-++--+-++++-+---+----+----+-++---+----++++-++-+--++--+++++--++++-------++--+++-
+-++---+-++-+-+---++++-+++++-+++--+++-++-++------++----++------+-++---++-+--+++++++++-+--+-+--++----
+---+--+-++----+++
---
-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
++---+--+------+++-----+-+++--+++++--++-++-----+++++++--++-+--+--+++---+--+-+++----++--+-++--++-+-+-
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
++-+-++-+-+---+-+++--+-+---+++----+-++++++++++-++++---++
+-+++----+-+++---
+-----+-++--+--++++++--++-++-+++++-++-+---+----------++-----+++-+-+-+---+-+-+--+---++-+--
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
++-++----+-+----+-+--+-++--+-----+-++++--+--++-----+---+++-+-+-++++++-+-+-++++++++-++---++--++--++--
+-+
---+-+------+-----+--+-+----+-----++--+++-+-+++-+-+-++-+++--++-+---+-----++-++-++++++-++++++-+-+-+-+
+-+-+-+-+-
-++------++---+---++-+-++-++--+-++-+---+++++++--++-+--+--+++--+----+--+++---++-+++++++-+-+-+--++----
++++--++-+--++---+-++--+---++-+-++++-++++--+-++--+++--+-+++--+-+--++-++--+----+--++-+-+++--+++++-+-+
-+--++-+---+++----++-+------+-+----+---+-+++-+++++-+-+-+-+++---+--++--+--++-+-++-++---++-+++---+-+--
-++++++++-
++-+++-++-+---+--+-+++++-+-++++++++--+--+-+--++-+---+++--+++--++-+++-+-+-+-+-+-++-
--++++++-----+-----+++------+--+++--+---++------+--+++-++-++++++--+++++-++-+-+-++++-+++-+-----+++++-
---+++++-+---+-+-+++++---+---+--+---
-+--+-
++
+-++++--+++--+--++---++--+-----++-+-+-+----+-++--+-++--++--+--++--++++-+++---+---+--+-+--+++--++-+--
+---+--+-++--++--+++--+----+---+-+++-+++-+---+--+++-+-+++++-++++-++--+++++-+++++--+--+-+++-+----+-+-
++-
-+-+-+-+-+
--+++++-++-+-+-+-+-+-+++++-++++------+--+-+--+++-+++--++++---+++-+--+--+-++--+------+--+--+-+-+--+--
-++++--++++--+-+-+-+-------+++----++-+-+---+-------+-----++---+-+++-+-+--+-+++++--++-+-+-+---++-+++-
+++-+-+-+--+-+++---++-++++-+-+-+++++---++-+++-+---++-++-+++-------+-++--+-+---+--+-+--+++--+--+-++--
+---+--+++--+++-+++++--++-+-+-++-+-++++-+++-++----+-++--+-+-----+-+++--+--+-++++--+--+++++++-------+
-+++--+-----++-++-+++++---+--+-++-+-++++---+-----++++++--+-+---+++--++-++--+-+-++--+--++-----+----+-
-+-
-----+-+-+-++++--+-+---++--++++++-++++-++++++++--++--+-+---++---+---++-+++-++-+----+----+--++---+---
+++----+--+--+---+++--+-++++++-++-----++-+++--+---+-+++-++--+++----------++++++-+---++--+-+-++--+++-
+-+-+----+-+---+-++++---+-+-++-+-+-+---++--+-+++-+++----+-+--++-+-++-++-++-++-+--
+
--++----+--+-++-+++-++-+-+-++-+-++-+--+-+++---+++--++++-++--+--++-++++-++--+++++-+--+-++---+++-+--+-""".split()

for i in xrange(len(things)):
    print "Case #%d: %d" %(i+1, flippy(things[i]))
    

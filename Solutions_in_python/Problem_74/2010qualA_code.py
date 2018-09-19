def strInt1DArrayConverter(arg):
    elements = arg.split(' ')
    result = []
    for i in range(len (elements)):
        result.append(int(elements[i]) if i % 2 is 0 else elements[i])
    return result
    
def dobot(bots, case, ibot):
    bot = bots[ibot]
    nextbot = None
    if not bot['done']:
        if bot['pos'] == bot['nxtbut']:
            if bot['next']:
                #print bot['name'], 'Press'
                i = bot['i'] + 2
                if i < len(case):
                    for xbot in bots:
                        if xbot['name'] == case[i]:
                            nextbot = xbot['name']
                    
                while i < len(case):
                    if case[i] == bot['name']:
                        bot['nxtbut'] = case[i+1]
                        bot['i'] = i
                        break
                    i += 2

                bot['done'] = i >= len(case)
            #else:
                #print bot['name'], 'Wait'
                
        else:
            bot['pos'] += 1 if bot['pos'] < bot['nxtbut'] else -1
            #print bot['name'], 'Move'
            
    return nextbot

def genbot(name):
    return {'name' : name,
            'done' : False,
            'pos' : 1,
            'nxtbut' : -1,
            'next' : False,
            'i' : -1
            }

def initbot(case, bot):
    bot['i'] = 1
    count = 0
    for i in range(1, len(case), 2):
        if case[i] == bot['name']:
            bot['nxtbut'] = case[i+1]
            bot['i'] = i
            bot['next'] = count is 0
            break
        count += 1
    bot['done'] =  bot['nxtbut'] < 0
            

import cjinput

root = 'C:\\codejam\\2011_qual_A'

cases = cjinput.cjinput(root + '\\input.in', root + '\\output.out')



for case in cases.testcases(converter = strInt1DArrayConverter):
    bots = [genbot('O'), genbot('B')]
    for bot in bots:
        initbot(case, bot)

    done = False
    turns = 0
    while not done:
        done = True
        nextbot = None
        for i in range(len(bots)):
            if nextbot == None:
                nextbot = dobot(bots, case, i)
            else:
                dobot(bots, case, i)
                
            done &= bots[i]['done']

        if nextbot:
            for bot in bots:
                bot['next'] = bot['name'] == nextbot

        turns += 1

    cases.writeoutput(turns)
            
            
        


        

'''
Created on Apr 8, 2017

@author: Admin
'''
def checkSort(inputlist):
    copylist = inputlist[:]
    copylist.sort()
    return copylist==inputlist

def checkGreater(x,y):
    return int(''.join(x))>int(''.join(y))

def getMaxTidyNumber():
    with open(r'F:\CodeJam2017\ProblemB\small.in','r') as rp:
        with open(r'F:\CodeJam2017\ProblemB\small.out','w') as wp:
            tcs = int(rp.readline())
            for tc in range(1,tcs+1):
                num = rp.readline().strip()
                if len(num)==1:
                    wp.write('Case #{}: {}\n'.format(tc,num))
                    continue
                orig = list(num)
                final = orig[:]
                dup = orig[:]
                dup.sort()
                if orig[0]==1 and all([i==0 for i in orig[1:]]):
                    num = int(num)-1
                    wp.write('Case #{}: {}\n'.format(tc,num))
                    continue
                if dup==orig:
                    wp.write('Case #{}: {}\n'.format(tc,num))
                    continue
                else:                   
                    for index,_ in enumerate(orig[::-1]):
                        #print('f',final,index)
                        if (len(orig)-index)<=2:
                            #print('in')
                            if orig[1]=='0':
                                final[1] = '9'
                                if orig[0]=='1':
                                    #print('u')
                                    final = final[1:]
                                    break
                                else:
                                    #print('no')
                                    final[0] = str(int(final[0])-1)
                                    break
                            else:
                                if int(orig[1])<int(orig[0]):
                                    final[1] = '9'
                                    final[0] = str(int(final[0])-1)
                                    break
                                else:
                                    if checkGreater(orig, final):
                                        break
                                    else:
                                        if final[1]=='9':
                                            if int(final[1])>int(final[0]):
                                                final[1] = str(int(final[1])-1)
                                            else:
                                                final[0] = str(int(final[0])-1)
                                        else:
                                            if final[1]>=final[0]:
                                                if not checkGreater(orig, final):
                                                    final[1]='9'
                                                    if not checkGreater(orig, final):
                                                        final[1] = str(int(orig[1])-1)
                                                        if final[1]<final[0]:
                                                            final[1] = '9'
                                                            final[0] = str(int(orig[0])-1)
                                               
                                                    
                                           
                            break
                                          
                        else:
                            if final[len(orig)-index-1] == '9':
                                continue
                            else:                                
                                final[len(orig)-index-1]='9'
                                if checkSort(final) and checkGreater(orig,final):
                                    break
                    
                    wp.write('Case #{}: {}\n'.format(tc,int(''.join([str(i) for i in final]))))
                     
def main():
    getMaxTidyNumber()

if __name__=='__main__':
    main()              
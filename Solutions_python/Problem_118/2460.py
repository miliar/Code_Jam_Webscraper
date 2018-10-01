import math
def fairsq(a,b):
    count=0
    for i in range(a,b+1):
        i_string=str(i)
        rev=i_string[::-1]
        if i_string==rev:
            root=0
            while root*root<i:
                root+=1
            if root*root==i:
                root_str=str(root)
                root_rev=root_str[::-1]
                if root_rev==root_str:
                    count+=1
                
        else:
            continue
    return count

def test():
    i=1
    file_handle=open('C-small-attempt0.in','r')
    T=int(file_handle.readline())
    while i<T+1:    
        spl=file_handle.readline().split()
        if len(spl)==2:
            a_str,b_str=spl
            a=int(a_str)
            b=int(b_str)
            print 'Case #' +str(i) +': ' +str(fairsq(a,b))
        i+=1
            

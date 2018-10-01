#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(L,X,unit_str):

    prod_dict={}
    
    prod_dict['11']={'dim':'1','sign':1}
    prod_dict['1i']={'dim':'i','sign':1}   
    prod_dict['1j']={'dim':'j','sign':1}       
    prod_dict['1k']={'dim':'k','sign':1}   

    prod_dict['i1']={'dim':'i','sign':1}
    prod_dict['ii']={'dim':'1','sign':-1}   
    prod_dict['ij']={'dim':'k','sign':1}       
    prod_dict['ik']={'dim':'j','sign':-1}   

    prod_dict['j1']={'dim':'j','sign':1}
    prod_dict['ji']={'dim':'k','sign':-1}   
    prod_dict['jj']={'dim':'1','sign':-1}       
    prod_dict['jk']={'dim':'i','sign':1}   

    prod_dict['k1']={'dim':'k','sign':1}
    prod_dict['ki']={'dim':'j','sign':1}   
    prod_dict['kj']={'dim':'i','sign':-1}       
    prod_dict['kk']={'dim':'1','sign':-1}   

    
    # おおまかな戦略
    ##    L文字をX回repeat
    ##    N=LX
    ##  どこぞで切れ目を入れ、そこまででleftmost substrがiになるかcheck
    ##  if yes, その後ろのどっかに切れ目を入れ、jとkになるかcheck
    ##   naiveにやると　O(N^3)?　ちょっと工夫できんかなあ。。。
    ##   
        
    # 先頭(0-origin) から (idx+1)個 分の substr の product を格納
    left_product_list=[]
    N=L*X
    
    if(N<3):
        return False
    
    
    org_list = unit_str*X
    #print org_list
    cur={'dim':'1','sign':1}
    for c in org_list:
        elem=prod_dict[cur['dim']+c].copy()
        elem['sign']*=cur['sign']
        left_product_list.append(elem.copy())
        cur=elem.copy()       

    # 末尾(0-origin) から(idx+1)個 分の substr の product を格納
    # rpl[0] = org[-1]
    # rpl[1] = org[-1]*org[-2]
    # rpl[i] = org[-1]*...*org[-(1+i)]
    right_product_list=[]
    cur={'dim':'1','sign':1}    
    for idx in range(len(org_list)):
        c = org_list[N-1-idx]
        elem=prod_dict[c+cur['dim']].copy()
        elem['sign']*=cur['sign']
        right_product_list.append(elem.copy())
        cur=elem.copy()
    #print right_product_list
    for idx,elem in enumerate(left_product_list):
        if elem['dim']=='i' and elem['sign']==1:
            #print "idx:", idx
            second_idx=idx+1
            # idx+1 .. second_idx  second_idx+1 ..末尾   が j と k になるかcheck
            cur={'dim':'1','sign':1}
            while(second_idx<N-1):
                elem=prod_dict[cur['dim']+org_list[second_idx]].copy()
                elem['sign']*=cur['sign']
                cur=elem.copy()

                #print "second_idx",second_idx
                #print "cur", cur                
                
                tmp_elem=right_product_list[N-2-second_idx]
                if tmp_elem['dim']=='k' and tmp_elem['sign']==1 and cur['dim']=='j' and cur['sign']==1:
                    return True
                else:
                    pass
                    #print "tmp_elem",tmp_elem
                second_idx+=1
        
    return False

if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        L,X = map(int,raw_input().strip().split())
        unit_str = raw_input().strip()
        ans=solve(L,X,unit_str)
        if ans:
            ans_str="YES"
        else:
            ans_str="NO"
        print("Case #%i: %s" % (caseNr, ans_str))

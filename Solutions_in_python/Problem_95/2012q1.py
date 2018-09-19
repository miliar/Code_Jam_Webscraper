#-------------------------------------------------------------------------------
# Name:        2012Q1
# Purpose:     Code Jam Entry
#
# Author:      Alex Louden 
# Website:     alexlouden.com
#
# Created:     15/04/2012
# Copyright:   (c) Alex Louden 2012
#-------------------------------------------------------------------------------

from string import split

def q1():
	
	sample_in = """ejp mysljylc kd kxveddknmc re jsicpdrysi
	rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
	de kr kd eoya kw aej tysr re ujdr lkgc jv"""
	
	sample_out = """our language is impossible to understand
	there are twenty six factorial possibilities
	so it is okay if you want to just give up"""
	
	charmap = {'z':'q','q':'z'}
	
	for i, char in enumerate(sample_in):
		charmap[char] = sample_out[i]
	
	string = """30
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi
tba ie vpelpyxxcpd ymtyad xkh jv bymmetccs ysi fbpkdrxyd
ejp feic uyx kd mkoc rbc varbylepcys rbcepcx
rbcpc kd se ysdtcp
ip qykjd ip qykjd ip qykjd ip qykjd eeeeeeeeeeeeb ip qykjd
k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja
njww rpasiyxcpc ysi yxjxj
aej oset aej tysr re
wep rbedc tbe dvcyo ks y resljc ie ser dvcyo re erbcp vcevmc
seneia jsicpdrysid rbcx dksfc rbca ypc dvcyoksl xadrcpkcd ks rbc dvkpkr
rpysdmyrksl rchr kd ser leped drpcslrb
drpcslrb kd leped drpcslrb
aej tysr dcmm rbksld yr xc neksl qeeex
ys cac wep ys cac ysi y vklces wep y vklces
mcr mkvd ie tbyr bysid ie
set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd
dtkwr yd rbc tksi zjkcr yd rbc wepcdr drcyia yd rbc xejsryks
pklbr k wepler bcpc ks rbc dryrcd aej fymm kr y dyjdylc ks rbc xejrb
eb seeeee lellymep kd bcyici wep rbc epvbysylc
eb xa lei mcrd xyoc ejr
vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd
ymm aejp nydc ypc ncmesl re cppep rbc dveesa nypi"""
	
	out = []
	for line in split(string, '\n')[1:]:
		newline = ''
		for char in line:
			newline+= charmap[char]
		out.append(newline)
	
	for i, sentence in enumerate(out,1):
		print "Case #{}: ".format(i) + sentence.strip()

def main():
    q1()

if __name__ == '__main__':
    main()
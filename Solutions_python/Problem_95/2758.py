s1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
s2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
s3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'

z1 = 'our language is impossible to understand'
z2 = 'there are twenty six factorial possibilities'
z3 = 'so it is okay if you want to just give up'

array1 = ['z','q']
array2 = ['q','z']
for i in range(len(s1)):
    if s1[i] not in array1 and s1[i] != ' ':
        array1.append(s1[i])
        array2.append(z1[i])

for i in range(len(s2)) :
    if s2[i] not in array1 and s2[i] != ' ':
        array1.append(s2[i])
        array2.append(z2[i])

for i in range(len(s3)):
    if s3[i] not in array1 and s3[i] != ' ':
        array1.append(s3[i])
        array2.append(z3[i])

string1 = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
rpysdmyrksl rchr kd ser leped drpcslrb
drpcslrb kd leped drpcslrb
set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd
eb seeeee lellymep kd bcyici wep rbc epvbysylc
eb xa lei mcrd xyoc ejr
kx fexxysicp dbcvypi ysi rbkd kd xa wygepkrc vpenmcx es rbc leelmc feic uyx
dtkwr yd rbc tksi zjkcr yd rbc wepcdr drcyia yd rbc xejsryks
ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi
rbkd kd de chfkrksl k bygc re le rbc nyrbpeex
wep rbedc tbe dvcyo ks y resljc ie ser dvcyo re erbcp vcevmc
seneia jsicpdrysid rbcx dksfc rbca ypc dvcyoksl xadrcpkcd ks rbc dvkpkr
eb acyb ympklbr tcpc lessy dbyoc kr jv tkrb rbc vypra ncyp resklbr
na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd
tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd
njww rpasiyxcpc ysi yxjxj
aej oset aej tysr re
rbkd bcpc kd ljsveticp yfrkgyrci rtcsra dcgcs fymkncp wjmm yjre se okfonyfo sykmrbpetksl xyabcx
ip qykjd ip qykjd ip qykjd ip qykjd eeeeeeeeeeeeb ip qykjd
xa syxc kd ijl k bygc ujdr xcr aej ysi k meeegc aej
kr tyd rbc ncdr ew rkxcd kr tyd rbc nmjpdr ew rkxcd
eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq
mcr mkvd ie tbyr bysid ie
"""
string2 = ""

for d in string1:
    try:
        i = array1.index(d)
        string2 = string2 + array2[i]
    except:
        string2 = string2 + d

print string2


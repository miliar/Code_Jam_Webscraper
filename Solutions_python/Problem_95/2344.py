

input = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv", "qz"]
output = ["our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up", "zq"]

diction = {}

for i in xrange(len(input)):
    statement = input[i]
    transl = output[i]
    for j in xrange(len(statement)):
        diction[statement[j]] = transl[j]

print diction, len(diction)
    
inp = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd
eb acyb ympklbr tcpc lessy dbyoc kr jv tkrb rbc vypra ncyp resklbr
wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso
bet ypc aej bemiksl jv ncfyjdc kx y veryre
aej tysr dcmm rbksld yr xc neksl qeeex
rbkd bcpc kd ljsveticp yfrkgyrci rtcsra dcgcs fymkncp wjmm yjre se okfonyfo sykmrbpetksl xyabcx
tba ie vpelpyxxcpd ymtyad xkh jv bymmetccs ysi fbpkdrxyd
rpysdmyrksl rchr kd ser leped drpcslrb
drpcslrb kd leped drpcslrb
kr tyd rbc ncdr ew rkxcd kr tyd rbc nmjpdr ew rkxcd
njww rpasiyxcpc ysi yxjxj
aej oset aej tysr re
kx fexxysicp dbcvypi ysi rbkd kd xa wygepkrc vpenmcx es rbc leelmc feic uyx
xa syxc kd ijl k bygc ujdr xcr aej ysi k meeegc aej
eb seeeee lellymep kd bcyici wep rbc epvbysylc
eb xa lei mcrd xyoc ejr
cyfb ew jd byd bkd ets dvcfkym lkwr ysi aej oset rbkd tyd xcysr re nc rpjc
ysi kw aej iesr jsicpcdrkxyrc xc k tesr jsicpcdrkxyrc aej
rbyso aej njr rbc pcym leelmcpcdc kd ks yserbcp fydrmc
set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd
eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq
ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi""".split('\n')


outp = ""
i = 1
for line in inp:
    outp += "Case #" + str(i) + ": "
    for letter in line:
        if diction.has_key(letter):      
            outp += diction[letter]
        else:
            outp += "?"
            
    i += 1
    outp += '\n'

print outp



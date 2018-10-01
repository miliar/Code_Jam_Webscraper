dict = {'a' : 'y',
        'b' : 'h',
        'c' : 'e',
        'd' : 's',
        'e' : 'o',
        'f' : 'c',
        'g' : 'v',
        'h' : 'x',
        'i' : 'd',
        'j' : 'u',
        'k' : 'i',
        'l' : 'g',
        'm' : 'l',
        'n' : 'b',
        'o' : 'k',
        'p' : 'r',
        'q' : 'z',
        'r' : 't',
        's' : 'n',
        't' : 'w',
        'u' : 'j',
        'v' : 'p',
        'w' : 'f',
        'x' : 'm',
        'y' : 'a',
        'z' : 'q'}

lines = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
kr tyd rbc ncdr ew rkxcd kr tyd rbc nmjpdr ew rkxcd
rpysdmyrksl rchr kd ser leped drpcslrb
drpcslrb kd leped drpcslrb
ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi
mcr mkvd ie tbyr bysid ie
pklbr k wepler bcpc ks rbc dryrcd aej fymm kr y dyjdylc ks rbc xejrb
xa syxc kd ijl k bygc ujdr xcr aej ysi k meeegc aej
eb seeeee lellymep kd bcyici wep rbc epvbysylc
eb xa lei mcrd xyoc ejr
eb acyb ympklbr tcpc lessy dbyoc kr jv tkrb rbc vypra ncyp resklbr
dtkwr yd rbc tksi zjkcr yd rbc wepcdr drcyia yd rbc xejsryks
set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd
rbkd bcpc kd ljsveticp yfrkgyrci rtcsra dcgcs fymkncp wjmm yjre se okfonyfo sykmrbpetksl xyabcx
vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd
ys cac wep ys cac ysi y vklces wep y vklces
set kd rbc djxxcp ew ejp myfo ew ikdfesrcsr
cyfb ew jd byd bkd ets dvcfkym lkwr ysi aej oset rbkd tyd xcysr re nc rpjc
ysi kw aej iesr jsicpcdrkxyrc xc k tesr jsicpcdrkxyrc aej
na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd
aej tysr dcmm rbksld yr xc neksl qeeex
k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja
tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd""".split("\n")

def translate():
    ret = []
    for line in lines:
        q = ''
        for c in line:
            if c == ' ':
                q += c
            else:
                q += dict[c]
        ret.append(q)
    return ret

result = translate()
case = 1
for res in result:
    print 'Case #' + str(case) + ': ' + res
    case += 1

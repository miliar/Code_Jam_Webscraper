import sys
class Logger(object):
        def __init__(self, filename="Default.log"):
            self.terminal = sys.stdout
            self.log = open(filename, "a")

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)
def jeu():
    fichier = open("C:\Users\Maroo_King\Downloads\A-large.in", "r")
    n= fichier.readline();
    n=int(n)
    ch=""
    for i in range(5*n-1):
        chi = fichier.readline();
        if (chi<>"\n"):
            ch+=chi[:4]
            
        
    i=0

    LO={"OOOO","OOOT","OOTO","OTOO","TOOO"}
    LX={"XXXX","XXXT","XXTX","XTXX","TXXX"}
    i=0
    for i in range(n) :
        chn=ch[:16]
        ch=ch[16:]
        LT={chn[:4],chn[4:8],chn[8:12],chn[12:],chn[0]+chn[4]+chn[8]+chn[12],chn[1]+chn[5]+chn[9]+chn[13],chn[2]+chn[6]+chn[10]+chn[14],chn[3]+chn[7]+chn[11]+chn[15],chn[0]+chn[5]+chn[10]+chn[15],chn[3]+chn[6]+chn[9]+chn[12]}
        rslt=''
        for j in LT :
            if (j in LO ):
                rslt="O won"
            elif (j in LX ):
                rslt="X won"
        if ((rslt == '') and ('.' in chn)):
            rslt="Game has not completed"
        elif (rslt=='') :
            rslt="Draw"
        ic=i+1
        ic=str(ic)
        pr= "Case #"+ic +": "+rslt
        
         
        
        
        print pr
sys.stdout = Logger("res.txt")
jeu()
   

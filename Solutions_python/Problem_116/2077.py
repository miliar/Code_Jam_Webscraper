def main():
    fi=open('A-large.in','r')
    line=fi.readline()
    line=line[:-1]
    t=int(line)
    op=''
    for x in range(t):
        rows=[]
        for y in range(4):
            temp=(fi.readline())
            rows.append(temp[:-1])
        cols=[]
        st=''
        for y in range(4):
            for z in rows:
                st=st+z[y]
            cols.append(st)
            st=''
        dia=[]
        temp=''
        for y in range(4):
            temp=rows[y]
            st=st+temp[y]
        dia.append(st)
        st=''
        temp=''
        for y in range(3,-1,-1):
            temp=rows[3-y]
            st=st+temp[y]
        dia.append(st)
        cells=[]
        for y in rows:
            for z in range(4):
                cells.append(y[z])
        al=dia+rows+cols
        if 'OOOT' in al or 'OOTO' in al or 'OTOO' in al or 'TOOO' in al or 'OOOO' in al:
            op=op+'Case #%d: O won\n'%(x+1)   
        elif 'XXXT' in al or 'XXTX' in al or 'XTXX' in al or 'TXXX' in al or 'XXXX' in al:
            op=op+'Case #%d: X won\n'%(x+1)
        elif '.' not in cells:
            op=op+'Case #%d: Draw\n'%(x+1)
        else:
            op=op+'Case #%d: Game has not completed\n'%(x+1)
        temp=fi.readline()
    fo=open('op.out','w')
    fo.write(op[:len(op)-1])
    fo.close()
    fi.close()
        


if __name__=="__main__":
    main()

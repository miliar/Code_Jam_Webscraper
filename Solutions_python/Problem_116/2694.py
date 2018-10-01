def ticTac(filePath):
    file=open(filePath,"r");
    #result=open("outputTicTac_large_input1.txt","a");
    #result=open("outputTicTac_large_input2.txt","a");
    result=open("outputTicTac_small_input.txt","a");
    data=file.readline().strip("\n");
    noOfTC=int(data);

    for x in range(0,noOfTC):
        line1=file.readline().strip("\n");
        line2=file.readline().strip("\n");
        line3=file.readline().strip("\n");
        line4=file.readline().strip("\n");
        diagonal_lr=[line1[0],line2[1],line3[2],line4[3]];
        diagonal_rl=[line1[3],line2[2],line3[1],line4[0]];
        vert1=[line1[0],line2[0],line3[0],line4[0]];
        vert2=[line1[1],line2[1],line3[1],line4[1]];
        vert3=[line1[2],line2[2],line3[2],line3[2]];
        vert4=[line1[3],line2[3],line3[3],line4[3]];
        board=[line1,line2,line3,line4,diagonal_lr,diagonal_rl,vert1,vert2,vert3,vert4];        
        #print (board);
        dotCount=0;
        resultt=False;
        resultStr="";
        for y in board:
            if("." not in y):
                if("X" in y and "O" not in y):
                    print("Case #"+str(x+1)+": X won");
                    result.write("Case #"+str(x+1)+": X won\n");
                    resultt=True;
                    break;
                elif("X" not in y and "O" in y):
                    print("Case #"+str(x+1)+": O won");
                    result.write("Case #"+str(x+1)+": O won\n");
                    resultt=True;
                    break;
            else:
                dotCount=dotCount+1;
        
        if(not resultt):
            if(dotCount>0):
                print("Case #"+str(x+1)+": Game has not completed");
                result.write("Case #"+str(x+1)+": Game has not completed\n");
            else:
                print("Case #"+str(x+1)+": Draw");
                result.write("Case #"+str(x+1)+": Draw\n");
    
          
        file.readline().strip("\n");

    file.close();
    result.close();


ticTac("C:\\GoogleCodeJam\\2013\\TicTac\\A-small-attempt1.in");


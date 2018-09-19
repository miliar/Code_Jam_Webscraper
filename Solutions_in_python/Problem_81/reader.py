class inpt :
  def __init__(self, filename) :
    f = open(filename,"r")
    self.string = f.read()
    self.f = open(filename.replace("input","output"),"w")

def getAll() :
  for i in ["ex","sm","lg"] :
    try :
      yield inpt(i + "_input.txt")
    except : 
      pass
  return

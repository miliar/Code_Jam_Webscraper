class mfw:
  """
  mfw : Multi-File With
  This utility class is a list of file handles.  It implements  __enter__
  and __exit__ methods so that it can be used via the with clause.
  """
  def __init__( self, *args ):
    self.handles = []
    for ( pathname, mode ) in args:
      self.handles.append( open( pathname, mode ) )

  def __enter__( self ):
    return self.handles

  def __exit__( self, type, value, traceback ):
    for handle in self.handles:
      handle.close()
